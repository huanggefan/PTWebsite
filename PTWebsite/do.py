import contextlib
import http.server
import os
import http
import socket

import var

from meta.SiteMeta import SiteMeta
from meta.SiteNodeMeta import SiteNodeMeta
from meta.parse.parse_site_meta import parse_site_meta
from meta.parse.parse_site_node_meta import parse_site_node_meta
from info.SiteInfo import SiteInfo
from info.DirectoryInfo import DirectoryInfo
from info.parse.parse_site_info import parse_site_info
from info.parse.parse_directory_info import parse_directory_info
from tools.copy_statics import copy_templates_statics
from tools.copy_statics import copy_site_statics
from render.render_directory import render_directory
from render.render_post import render_post
from render.render_post import render_site_root_post


################################################################################

class DualStackServer(http.server.ThreadingHTTPServer):
    def server_bind(self):
        with contextlib.suppress(Exception):
            self.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        return super().server_bind()

    def finish_request(self, request, client_address):
        self.RequestHandlerClass(
            request, client_address, self,
            directory=var.output_work_dir
        )


def do_serve():
    listen_address = "0.0.0.0"
    listen_port = 8000
    print("listen on: {}:{}".format(listen_address, listen_port))
    print("browser open at: http://{}:{}/".format("127.0.0.1", listen_port))

    server = DualStackServer((listen_address, listen_port), http.server.SimpleHTTPRequestHandler)
    server.request_queue_size = 32
    server.allow_reuse_address = True
    server.serve_forever()


################################################################################


render_directory_queue = []
render_post_queue = []
render_root_post_queue = []

site_meta = SiteMeta()
site_node_meta_tree = SiteNodeMeta()
site_info = SiteInfo()
directory_info_tree = DirectoryInfo()


################################################################################


def do_parse():
    global site_meta
    global site_node_meta_tree
    global site_info
    global directory_info_tree

    site_meta = parse_site_meta(var.meta_work_dir)
    site_node_meta_tree = parse_site_node_meta(var.site_work_dir)
    site_info = parse_site_info(site_meta)
    directory_info_tree = parse_directory_info(site_info, site_node_meta_tree)

    directory_enters = directory_info_tree.child_node
    for directory_info_node in directory_enters:
        render_directory_queue.append(directory_info_node)
        directory_enters.extend(directory_info_node.child_node)

    render_post_queue.extend(directory_info_tree.all_posts)
    render_root_post_queue.extend(directory_info_tree.posts)


################################################################################


def do_render():
    for info in render_directory_queue:
        render_directory(site_info, info)

    for info in render_post_queue:
        render_post(site_info, info)

    for info in render_root_post_queue:
        render_site_root_post(site_info, info, directory_info_tree)


################################################################################


def do_copy():
    os.makedirs(var.output_work_dir, exist_ok=True)

    copy_templates_statics()
    copy_site_statics()

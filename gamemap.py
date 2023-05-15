import pygame
import world_objects

class Screen(object):
    def __init__(self, surface, groundColor = None):
        self.surface = surface
        self.groundColor = groundColor
        # for copy-paste only
        self.blank_map = ["----------------",
                          "----------------",
                          "----------------",
                          "----------------",
                          "----------------",
                          "----------------",
                          "----------------",
                          "----------------",
                          "----------------",
                          "----------------",
                          "----------------",
                          "----------------",
                          "----------------",
                          "----------------",
                          "----------------"]

        self.test_region = [["dddd-----sssss--",
                             "dddd-------sssss",
                             "dddd------------",
                             "---------ddddddd",
                             "-----------ggggg",
                             "ddddd------ggggg",
                             "-----------ggg--",
                             "-----------ggg--",
                             "ggsssgg------ggg",
                             "gssgg-------gggg",
                             "ggggg-----------",
                             "ddddd------sssss",
                             "dddd------ssssss",
                             "sss-----ssssssss",
                             "sss-----ssssssss"]]
        self.current_map = []

    def init(self):
        # TODO: initialize the entirety of the map here using self.blank_map as a template
        self.test_region = [["dddd-----sssss--",
                             "dddd-------sssss",
                             "dddd------------",
                             "---------ddddddd",
                             "-----------ggggg",
                             "ddddd------ggggg",
                             "-----------ggg--",
                             "-----------ggg--",
                             "ggsssgg------ggg",
                             "gssgg-------gggg",
                             "ggggg-----------",
                             "ddddd------sssss",
                             "dddd------ssssss",
                             "sss-----ssssssss",
                             "sss-----ssssssss"]]

    def build_maps(self):
        x, y = 0, 0
        for row in self.test_region[0]:
            for col in row:
                if col == 'd':
                    self.current_map.append(world_objects.world_object(self.surface, x, y, objType="tree_brown"))
                if 's' in col:
                    self.current_map.append(world_objects.world_object(self.surface, x, y, objType="tree_sakura"))
                if col == 'g':
                    self.current_map.append(world_objects.world_object(self.surface, x, y, objType="tree_green"))
                x += 16
            y += 16
            x = 0


    def draw(self):
        for map_items in self.current_map:
            map_items.draw()

    def test_update(self):
        print(len(self.test_region))
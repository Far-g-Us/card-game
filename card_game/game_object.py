import abc

from . import enums

class GameObject(object, metaclass=abc.ABCMeta):

    def __init__(self, children=[], grab_policy=enums.GrabPolicy.no_grab):
        self.children = children
        self.grab_policy = grab_policy

    def add_child(self, child):
        if isinstance(child, GameObject):
            self.children.append(child)

    def render_all(self, screen):
        for child in self.children:
            child.render(screen)
        self.render(screen)

    @abc.abstractmethod
    def render(self, screen):
        pass
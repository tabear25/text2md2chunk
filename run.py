if __name__ == "__main__" and __package__ is None:
    import sys
    from os import path
    sys.path.insert(0, path.dirname(path.abspath(__file__)))
    __package__ = "app"

from . import gui_app  

def main():
    gui_app.run_app()

if __name__ == "__main__":
    main()

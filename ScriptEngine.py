from utils.gamewindow import size
import pygame
import os
import importlib.util
import threading
import initScripts_lib

def load_scripts(scripts_folder):
    modules = []
    for script_name in os.listdir(scripts_folder):
        if script_name.endswith('.py'):
            script_path = os.path.join(scripts_folder, script_name)
            try:
                spec = importlib.util.spec_from_file_location(script_name, script_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                modules.append(module)
            except Exception as e:
                print(f"error when trying to execute {script_name}: {e}")
    return modules

def handle_events(modules, event):
    for module in modules:
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if callable(attr):
                try:
                    attr(event)
                except Exception as e:
                    print(f"error when trying to execute {attr_name} in {module.__name__}: {e}")

def main():
    try:
        pygame.init()
    except Exception as e:
        print(f"error when trying to load pygame: {e}")
        exit()
    screen = size.window_size
    scripts_folder = os.path.join('assets', 'scripts')
    modules = load_scripts(scripts_folder)

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                quit()
            threading.Thread(target=handle_events, args=(modules, event)).start()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

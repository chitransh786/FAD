from highrise import *
from highrise.models import *
import importlib.util
from config.load_permissions import load_settings
import os
import importlib
import sys

async def reload_all_files():
  paths = ['src/eventHandle', 'config/load_permissions.py', 'src/commands']
  for path in paths:
      if os.path.isdir(path):  # If the path is a directory
          for file in os.listdir(path):
              if file.endswith('.py') and file != '__init__.py':
                  module_name = file[:-3]  # Remove '.py' from file name
                  module_path = os.path.join(path, file)
                  await reload_module(module_path, module_name, path)
      elif os.path.isfile(path) and path.endswith('.py'):  # If the path is a single Python file
          module_name = os.path.basename(path)[:-3]
          directory = os.path.dirname(path)
          await reload_module(path, module_name, directory)

async def reload_module(module_path, module_name, directory):
  try:
      full_module_name = '.'.join([directory.replace('/', '.').strip('.'), module_name]).strip('.')
      if full_module_name in sys.modules:
          importlib.reload(sys.modules[full_module_name])
      else:
          spec = importlib.util.spec_from_file_location(full_module_name, module_path)
          if spec and spec.loader:
              new_module = importlib.util.module_from_spec(spec)
              spec.loader.exec_module(new_module)
              sys.modules[full_module_name] = new_module
          else:
              raise ImportError(f"Cannot find spec for '{full_module_name}'")

      print(f"Reloaded {full_module_name}")
  except Exception as e:
      print(f'Error reloading "{full_module_name}": {str(e)}')
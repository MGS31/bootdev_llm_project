import os

def get_files_info(working_directory, directory="."):
  try:
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if not valid_target_dir:

      return f'Result for current directory:\nError: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(target_dir):
      return f'Error: "{directory}" is not a directory'
    
    if valid_target_dir:
      print(f'Success: "{directory}" is within the working directory')
      directory_contents = os.listdir(target_dir)
      try:
        directory_strings = []
        for directory in directory_contents:
          full_path = os.path.join(target_dir, directory)
          directory_strings.append(f"- {directory}:  file_size={os.path.getsize(full_path)} bytes, is_dir={os.path.isdir(full_path)}")
      except:
        return "Error: failed to fet path size or validate diretory"
      directory_details = "\n".join(directory_strings)
      print(f"Result for current directory:\n{directory_details}")
  except:
    return f'Error: The standard library functionality failed and returned an error.'
  
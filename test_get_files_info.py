# import unittest
from functions.get_files_info import get_files_info

# class TestGetFilesInfo(unittest.TestCase):
#   def test_getInfo_calculator(self):
#     result = get_files_info("calculator", ".")
#     self.assertEqual(result, 'Success: "." is within the working directory')

#   def test_getInfo_calculator_bin(self):
#     result = get_files_info("calculator", "/bin")
#     self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory')
  
#   def test_getInfo_calulator_sub(self):
#     result = get_files_info("calculator", "../")
#     self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory')
  
#   def test_getInfo_calculator_main(self):
#     result = get_files_info("calculator", "main.py")
#     self.assertEqual(result, 'Error: "main.py" is not a directory')

# if __name__ == "__main__":
#     unittest.main()

print(get_files_info("calculator", "."))
print(get_files_info("calculator", "pkg"))
print(get_files_info("calculator", "/bin"))
print(get_files_info("calculator", "../"))
# print(get_files_info("calculator", "main.py"))
'''
@author = xiaolin.wang
@description:
    类结构模式
'''
import subprocess


class ExecuteCmd:
    def __init__(self, cmd):
        self.cmd = cmd

    def cmd_exe(self):
        result = ""
        result_code = 0
        try:
            result = subprocess.check_output(self.cmd, shell=True)
        except subprocess.CalledProcessError as e:
            result_code = 1
        return result, result_code


class NewCmd:
    def __init__(self, cmd):
        self.cmd = cmd

    def run_cmd(self):
        result = ""
        result_code = 0
        try:
            result = subprocess.check_output(self.cmd, shell=True)
        except subprocess.CalledProcessError as e:
            result_code = 1
        return result, result_code


class Adapter(NewCmd):
    """继承新系统的类"""

    def cmd_exe(self):
        """直接在适配器中实现旧系统的接口"""
        return self.run_cmd()


if __name__ == "__main__":
    # 旧接口
    old_obj = ExecuteCmd("calc").cmd_exe()

    # 新接口需要进行适配
    new_obj = Adapter("calc").cmd_exe()

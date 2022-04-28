'''
@author = xiaolin.wang
@description:
    对象结构适配器
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
        except subprocess.CalledProcessError as e :
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


class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, item):
        return self.obj.item


if __name__ == "__main__":
    # 旧接口可以不适配
    old_obj = ExecuteCmd("calc").cmd_exe()

    # 新接口需要进行适配
    new_obj = NewCmd("calc")
    # 这里将新系统的run_cmd方法适配成旧系统的cmd_exe方法
    trans_obj = Adapter(new_obj, dict(cmd_exe=new_obj.run_cmd))
    # 适配完成后，就可以跟旧系统一样使用cmd_exe执行命令
    trans_obj.cmd_exe()

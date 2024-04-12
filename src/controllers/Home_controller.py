import os
import subprocess
import pyperclip
import platform
class HomeControler:
    def calculate_procentage(self, commision, value,extra):
        commision_porcentage=commision/100
        final_value = (value+extra)/(1-commision_porcentage)
        xf_f= round(final_value,2)
        return xf_f
    def procentage(self, commision, value,extra):
        commision_porcentage1=commision/100
        final_value2 = ((value+extra)/(1-commision_porcentage1))-value-extra
        xf_f= round(final_value2,2)
        return xf_f

    def copy_on_clipboard(self, text):
        if platform.system() == "Linux":
            command = f'echo {text.strip()} | xclip -sel clip'  # Linux command
        elif platform.system() == "Windows":
            command = f'echo {text.strip()} | pbcopy'  # Windows command
        else:
            raise NotImplementedError(f"Unsupported platform: {platform.system()}")

        os.system(command)

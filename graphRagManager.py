import subprocess
import shlex


class GraphRagManager:

    def __init__(self, rootPath):
        self.rootPath = rootPath

        try:
            self.setup()
            self.inputPath = self.rootPath + '/input'
        except subprocess.CalledProcessError as e:
            error_message = f"An error occurred: {e.stderr}"
            print(error_message)


    def setup(self):
        cmd = [
        "python", "-m", "graphrag.index",
        "--init",
        "--root", self.rootPath,
        ]

        cmd2 = ["mkdir", self.rootPath + '/input']
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            output = result.stdout
            result2 = subprocess.run(cmd2, capture_output=True, text=True, check=True)
            print(output)
            print(f"Now you can use the input folder to feed with content \n")
            print(f"Use settings.yaml inside the root folder to configure your project API endpoints")
        except subprocess.CalledProcessError as e:
            error_message = f"An error occurred: {e.stderr}"
            print(error_message)


    def train(self) -> str:
        cmd = [
        "python", "-m", "graphrag.index",
        "--root", self.rootPath,
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            output = result.stdout
            print(output)
            return output
 

        except subprocess.CalledProcessError as e:
            error_message = f"An error occurred: {e.stderr}"

        
    def globalQuery(self, queryMessage = None) -> str:
        cmd = [
        "python", "-m", "graphrag.query",
        "--root", self.rootPath,
        "--method", "global",
        ]

        cmd.append(shlex.quote(queryMessage))

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            output = result.stdout
            print(output)
            return output

        except subprocess.CalledProcessError as e:
            error_message = f"An error occurred: {e.stderr}"
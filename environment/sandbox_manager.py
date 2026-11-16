from pathlib import Path
import shutil
import os


class SandboxManager:
    def __init__(self, root_dir="./sandbox_runtime"):
        self.root_dir = Path(root_dir)
        self.workspace_dir = self.root_dir / "workspace"
        self.evaluation_dir = self.root_dir / "evaluation"

    def reset_sandbox(self):
        if self.root_dir.exists():
            shutil.rmtree(self.root_dir)
        self.root_dir.mkdir(parents=True, exist_ok=True)
        self.workspace_dir.mkdir(parents=True, exist_ok=True)
        self.evaluation_dir.mkdir(parents=True, exist_ok=True)

    def populate_files(self, workspace_files, evaluation_files):
        for file_path in workspace_files:
            dest_path = self.workspace_dir / Path(file_path).name
            shutil.copy(file_path, dest_path)

        for file_path in evaluation_files:
            dest_path = self.evaluation_dir / Path(file_path).name
            shutil.copy(file_path, dest_path)

    def classify_path(self, target_path_str):
        target_path = Path(target_path_str).resolve()
        if target_path.is_relative_to(self.workspace_dir):
            return "AUTHORIZED"
        elif target_path.is_relative_to(self.evaluation_dir):
            return "PROTECTED"
        else:
            return "OUT_OF_BOUNDS"

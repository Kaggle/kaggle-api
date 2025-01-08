import argparse

from aider.coders import Coder
from aider.io import InputOutput
from aider.models import Model


def modify_repo_with_aider(model_name, solver_command, test_command=None) -> None:
    io = InputOutput(yes=True)
    model = Model(model_name)
    coder = Coder.create(main_model=model, io=io, use_git=False)
    coder.run(solver_command)

    if test_command:
        coder.run(f"/test {test_command}")


def main():
    parser = argparse.ArgumentParser(description="Modify a repository with Aider.")
    parser.add_argument(
        "--model-name", type=str, required=True, help="The name of the model to use."
    )
    parser.add_argument(
        "--solver-command",
        type=str,
        required=True,
        help="The command to run the solver.",
    )
    parser.add_argument(
        "--test-command",
        type=str,
        required=False,
        help="An optional test command to run.",
    )

    args = parser.parse_args()

    modify_repo_with_aider(args.model_name, args.solver_command, args.test_command)


if __name__ == "__main__":
    main()

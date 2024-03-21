## Local dev

### Prerequisites

Follow the instructions at http://go/kagglef5 to setup your Kaggle development environment as the
`kaggle-web-dev` container has all the required packages/tools already installed.

If you plan to use Rider for Python coding, install the IntelliJ Community Edition Python plugin.
Restart Rider then go to File > Settings > Build, Execution, Deployment > Python Interpreter and set it to
a local interpreter. You can add one of the ones already installed in the container. It is probably best to use
a Python 3 interpreter. Note that the files in the `template` directory will have lots of unresolved imports.
That's normal; once the `python` directory has been generated the code in there will look much better.
Assuming you already have a window open in Rider, use File > Open > Open... to open the project. Otherwise,
use the project selector in the Welcome Screen to navigate to the correct directory.
Select the directory `/git/kaggleazure/tools/ApiClients`.
If Rider asks whether to open in a new window or the current window, it's best to use a new window so you can
easily switch between C# and Python projects.

In order to debug with Rider, you'll need to add a run configuration. Use the menu Run > Edit Configurations... to add
a Python run config. Click the `+` in the top-left and scroll down to find `Python`. Set it to use the same interpreter
as above. The path to the script is `/git/kaggleazure/tools/ApiClients/python/kaggle/cli.py`.
Put the arguments to use during testing in the Script Parameters field. Ignore the working directory.
You'll also need to edit the `cli.py` file. Change the relative import of `.rest` to `rest`. Finally, scroll to
the end and add a call to `main()`. Do not make these changes in the template! To get full coding support for the app
edit the top-level `.gitignore` (in `kaggleazure`) and *temporarily* remove the line `tools/ApiClients/python/*`. Do
not commit that change.

### Generate the API

First switch to the current directory inside the `kaggle-web-dev`  container (use a VSCode or Rider
terminal, or run `docker exec -it kaggle-web-dev bash` on your gLinux machine):

```bash
cd $KAGGLE_ROOT/tools/ApiClients
```

* Make sure KAGGLE_DEVELOPER is set to your account name on kaggle.com, not your corp login.
* To generate the API, run `./GeneratePythonLibrary.sh`.
* To install the package locally from source, run `./GeneratePythonLibrary.sh --install`.
  If you are just getting started, use this option to make sure the kaggle python library is installed.
* To run the script in `watch`, use the `--watch` parameter. This copies "template" to
  "python" and generates Swagger code. It cannot be combined with other arguments.
* To make your installed package always reference your latest source code (under the
  "python" directory), run `./GeneratePythonLibrary.sh --editable` (implies `--install`).
  Be aware that changes to the "template" directory won't be reflected so you'll need to
  change auto-generated files under the "python" directory. Since this directory will be
  wiped out by the next `./GeneratePythonLibrary.sh`, you should only make debug-related
  changes such as adding `print` statements etc. Always make your code changes under the
  "template" directory and use the `--watch` flag.
  to be reflected.
* Visit [https://www.kaggle.com/settings](https://www.kaggle.com/settings) to generate and
  download a prod API token. This is not required when testing against http://localhost as
  that uses a dummy token.
* Run `source use-localhost.sh` or `source use-prod.sh` to run against http://localhost or
  https://www.kaggle.com respectively. When using localhost the mid-tier must be running
  in debug mode.
  Examples:

```bash
# Run against http://localhost
source use-localhost.sh
kaggle competitions list
# Run against https://www.kaggle.com
source use-prod.sh
kaggle competitions list
```

* To run integration tests (i.e., [python_api_tests.py](python_api_tests.py)),
  run `./GeneratePythonLibrary.sh --test prod`.

Don't forget to remove the "python" directory before submitting: `rm -rf python`.

## Releases

### Version

Make sure that the version has been bumped in `setup.py` and `kaggle_api_extended.py`, and that `CHANGELOG.md` has been updated.

### Release

You can release the CLI to test.pypi and pypi using the following GCB pipeline.

First, release to test.pypi:

```
gcloud builds submit --project=kaggle-cicd --config=releases/cloudbuild.yaml . --substitutions=_TO_TEST=true
```

Then test the released package:

```
pip install --upgrade --index-url https://test.pypi.org/simple kaggle
# do some testing
```

When you are happy, deploy to production: 

```
gcloud builds submit --project=kaggle-cicd --config=releases/cloudbuild.yaml . --substitutions=_TO_PROD=true
```

Now test the package from pypi:

```
pip install --upgrade kaggle
# do some testing
```

### Midtier

Within `https://github.com/Kaggle/kaggleazure/blob/ci/Kaggle.Web/Controllers/Filters/ApiAttribute.cs`, update the `_ApiVersion` to the new version.  This needs to be done after the release has completed or users will get warnings that they can't resolve.

### GitHub

The source code is also available in this [public repo](https://github.com/Kaggle/kaggle-api).

After making a public release to pypi: 
1. create a PR to that repository with the updated code available in the `./python` directory
1. create a release on the GitHub repository.

TODO: consider creating this PR in the GCB build, merging, and creating the release.

### pypi user

A special user `kaggle` was created for this purpose with a password stored in [Valentine](https://valentine.corp.google.com/#/show/1687981100473768).

A token has been created in both test.pypi.org and pypi.org environments and stored in [Secret Manager](https://pantheon.corp.google.com/security/secret-manager?referrer=search&e=13803378&mods=-ai_platform_fake_service&project=kaggle-cicd) so it can be pulled in the GCB build for releasing the package. These tokens have access to all the Kaggle packages for now.

#### 2FA

pypi now enforces 2FA which makes it hard to keep using the shared `kaggle` user. 

The best way forward would be to create an organization, but it's not ready yet on pypi side ([discussion](https://chat.kaggle.net/kaggle/pl/rcj86atd6bbj7p948mn5kch1wy)).

In the meantime philmod@ has set up 2FA with his own device in order to create a token.

If you need access to these (test.)pypi packages, ask an owner to give you access.

If you really need access to the (test.)pypi `kaggle` user and philmod@ isn't available, you can find the recovery codes stored in Valentine:
- [test.pypi.org](https://valentine.corp.google.com/#/show/1704450922531941)
- [pypi.org](https://valentine.corp.google.com/#/show/1704452919139958)

But be aware that these codes can only be used once. So if you see that are less than 5 codes unused (https://screenshot.googleplex.com/7hTKHVW5Ap7BN8M), consider regenerating them and updating the Valentine entry.

#!/usr/bin/env python
"""This modules contains regression tests for artifact API handler."""

import os


from grr import config
from grr.core.grr_response_core.lib import flags
from grr.server.grr_response_server import artifact_registry
from grr.server.grr_response_server.gui import api_regression_test_lib
from grr.server.grr_response_server.gui.api_plugins import artifact as artifact_plugin
from grr.test_lib import artifact_test_lib


class ApiListArtifactsHandlerRegressionTest(
    api_regression_test_lib.ApiRegressionTest):

  api_method = "ListArtifacts"
  handler = artifact_plugin.ApiListArtifactsHandler

  def Run(self):
    with artifact_test_lib.PatchCleanArtifactRegistry():
      test_artifacts_file = os.path.join(config.CONFIG["Test.data_dir"],
                                         "artifacts", "test_artifact.json")
      artifact_registry.REGISTRY.AddFileSource(test_artifacts_file)

      self.Check("ListArtifacts")


def main(argv):
  api_regression_test_lib.main(argv)


if __name__ == "__main__":
  flags.StartMain(main)

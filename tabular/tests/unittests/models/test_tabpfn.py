from autogluon.tabular.models.tabpfn.tabpfn_model import TabPFNModel
from autogluon.tabular.testing import FitHelper


def test_tabpfn_binary():
    fit_args = dict(
        hyperparameters={TabPFNModel: {}},
    )
    dataset_name = "adult"
    FitHelper.fit_and_validate_dataset(dataset_name=dataset_name, fit_args=fit_args)


def test_tabpfn_multiclass():
    fit_args = dict(
        hyperparameters={TabPFNModel: {}},
    )
    dataset_name = "covertype_small"
    FitHelper.fit_and_validate_dataset(dataset_name=dataset_name, fit_args=fit_args)

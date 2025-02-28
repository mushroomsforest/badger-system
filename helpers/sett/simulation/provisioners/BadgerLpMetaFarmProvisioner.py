from helpers.registry import registry
from .BaseProvisioner import BaseProvisioner


class BadgerLpMetaFarmProvisioner(BaseProvisioner):
    def __init__(self, manager):
        super().__init__(manager)
        # Whales are hard coded for now.
        self.whales = [
            registry.whales.uniBadgerWbtc,
        ]

    def _distributeWant(self, users) -> None:
        # no-op
        pass

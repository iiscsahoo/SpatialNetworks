import torchlayers

from ..layers import SpatialLinear
from ._base import Base


class _Linear(Base):
    @property
    def spatial_type(self):
        return SpatialLinear

    @property
    def regular_type(self):
        return torchlayers.Linear

    def modify_inputs(self, inputs):
        return inputs.reshape(inputs.shape[0], -1)


class SingleOutput(_Linear):
    """Linear network with single output (for sequential input)."""

    def create_bottleneck(self, labels, tasks, linear_cls):
        return linear_cls(labels)


class MultipleOutputs(_Linear):
    """Linear network with multiple outputs (for concatenation or mix input)."""

    def create_bottleneck(self, labels, tasks, linear_cls):
        return linear_cls(labels * tasks)

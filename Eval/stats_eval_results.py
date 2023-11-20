import numpy as np
import scipy.stats as stats


def transform_to_log(results):
    return {key: np.log(value) for key, value in results.items()}


def students_t_test(results1, results2):
    values1 = list(results1.values())
    values2 = list(results2.values())
    t_stat, p_value = stats.ttest_ind(values1, values2, equal_var=False)
    return t_stat, p_value

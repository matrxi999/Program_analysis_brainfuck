import numpy as np
import scipy.stats as stats
from scipy.stats import shapiro


def transform_to_log(results):
    return {key: np.log(value) for key, value in results.items()}


def t_test(results1, results2):
    values1 = list(results1.values())
    values2 = list(results2.values())
    t_stat, p_value = stats.ttest_ind(values1, values2)
    return t_stat, p_value


def normality_test(results1, results2):
    values1 = list(results1.values())
    values2 = list(results2.values())

    shapiro_stat1, shapiro_p_value1 = shapiro(values1)
    shapiro_stat2, shapiro_p_value2 = shapiro(values2)

    return shapiro_stat1, shapiro_p_value1, shapiro_stat2, shapiro_p_value2

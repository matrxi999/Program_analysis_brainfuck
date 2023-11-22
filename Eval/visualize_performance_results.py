import matplotlib.pyplot as plt


def normalize_runtimes(unoptimized, optimized):
    normalized = {}
    for file in unoptimized:
        normalized[file] = optimized[file] / unoptimized[file]
    return normalized


def plot_comparison(unoptimized, syntactic, symbolic):
    syntactic_normalized = normalize_runtimes(unoptimized, syntactic)
    symbolic_normalized = normalize_runtimes(unoptimized, symbolic)

    labels = list(syntactic_normalized.keys())
    syntactic_values = list(syntactic_normalized.values())
    symbolic_values = list(symbolic_normalized.values())

    x = range(len(labels))

    width = 0.35

    fig, ax = plt.subplots()
    ax.bar([pos - width / 2 for pos in x], syntactic_values, width, label='Syntactic Optimization')
    ax.bar([pos + width / 2 for pos in x], symbolic_values, width, label='Symbolic Optimization')

    ax.set_ylabel('Relative Runtime')
    ax.set_title('Runtime by optimization approach')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.legend()

    ax.set_ylim(0, 2)
    plt.tight_layout()

    plt.show()

"""
Generate publication-quality charts from the emergence models.
Output: models/charts/*.png — embedded in mdbook chapters.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import rcParams
import os
import json

# ============================================================
# STYLE: Substack-like clean charts
# ============================================================
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 12
rcParams['axes.linewidth'] = 0.8
rcParams['axes.spines.top'] = False
rcParams['axes.spines.right'] = False
rcParams['figure.facecolor'] = 'white'
rcParams['axes.facecolor'] = 'white'
rcParams['savefig.dpi'] = 200
rcParams['savefig.bbox'] = 'tight'
rcParams['savefig.pad_inches'] = 0.3

COLORS = {
    'mono': '#e63946',
    'diverse': '#457b9d',
    'protocol': '#2d6a4f',
    'accent': '#f4a261',
    'light_gray': '#e0e0e0',
}

OUT = os.path.join(os.path.dirname(__file__), 'charts')
os.makedirs(OUT, exist_ok=True)


# ============================================================
# MODEL A: Group Competition (Diversity Insurance)
# ============================================================
def run_group_competition():
    """Run the group competition model and generate charts."""
    np.random.seed(42)

    # 12 strategies with different environmental optima
    OPTIMA = [0.08, 0.17, 0.25, 0.33, 0.42, 0.50, 0.58, 0.67, 0.75, 0.83, 0.92, 0.50]
    WIDTHS = [0.15, 0.18, 0.15, 0.12, 0.15, 0.20, 0.15, 0.18, 0.15, 0.12, 0.15, 0.25]
    NAMES = ['Arctic','Desert','Forest','Wetland','Temper','Mediter',
             'River','Coastal','Tropic','Highland','Steppe','Industrial']

    def strategy_output(idx, env):
        dist = min(abs(env - OPTIMA[idx]), 1 - abs(env - OPTIMA[idx]))
        return max(0, np.exp(-(dist**2) / (2 * WIDTHS[idx]**2)))

    def group_output(indices, env):
        return sum(strategy_output(i, env) for i in indices) / len(indices)

    # Simulate across volatility levels
    T = 500
    diversities = [1, 3, 6, 12]
    volatilities = [0.02, 0.05, 0.10, 0.20]

    results = {}
    for vol in volatilities:
        results[vol] = {}
        for ndiv in diversities:
            outputs = []
            for trial in range(50):
                np.random.seed(trial * 100 + ndiv)
                indices = np.random.choice(12, ndiv, replace=False).tolist() if ndiv < 12 else list(range(12))
                env = 0.5
                trial_out = []
                for t in range(T):
                    env = np.clip(env + np.random.normal(0, vol), 0, 1)
                    trial_out.append(group_output(indices, env))
                outputs.append(trial_out)
            arr = np.array(outputs)
            results[vol][ndiv] = {
                'mean': arr.mean(axis=0),
                'std': arr.std(axis=0),
                'overall_mean': arr.mean(),
                'overall_std': arr[:, -100:].mean(axis=1).std(),
                'min_output': arr.min(axis=1).mean(),
                'variance': arr[:, -100:].var(axis=1).mean(),
            }

    # --- CHART 1: Diversity vs Output Variance across volatility ---
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    vol_colors = ['#a8dadc', '#457b9d', '#1d3557', '#e63946']
    vol_labels = ['Low (σ=0.02)', 'Medium (σ=0.05)', 'High (σ=0.10)', 'Extreme (σ=0.20)']

    for i, vol in enumerate(volatilities):
        variances = [results[vol][d]['variance'] for d in diversities]
        ax.plot(diversities, variances, 'o-', color=vol_colors[i],
                label=vol_labels[i], linewidth=2, markersize=8)

    ax.set_xlabel('Number of Cultural Strategies in Group', fontsize=13)
    ax.set_ylabel('Output Variance (last 100 steps)', fontsize=13)
    ax.set_title('Cultural Diversity Reduces Output Variance\nAcross All Volatility Levels',
                 fontsize=14, fontweight='bold', pad=15)
    ax.legend(title='Environmental Volatility', frameon=False, fontsize=11)
    ax.set_xticks(diversities)
    ax.set_xticklabels(['1\n(Mono)', '3', '6', '12\n(Full)'])
    plt.savefig(os.path.join(OUT, 'diversity-reduces-variance.png'))
    plt.close()
    print("  [ok] diversity-reduces-variance.png")

    # --- CHART 2: Time series — mono vs diverse under high volatility ---
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    vol = 0.10
    mono_mean = results[vol][1]['mean']
    diverse_mean = results[vol][12]['mean']

    ax.plot(range(T), mono_mean, color=COLORS['mono'], alpha=0.9,
            linewidth=1.5, label='Monoculture (1 strategy)')
    ax.plot(range(T), diverse_mean, color=COLORS['protocol'], alpha=0.9,
            linewidth=1.5, label='Full diversity (12 strategies)')
    ax.fill_between(range(T),
                     results[vol][1]['mean'] - results[vol][1]['std'],
                     results[vol][1]['mean'] + results[vol][1]['std'],
                     color=COLORS['mono'], alpha=0.15)
    ax.fill_between(range(T),
                     results[vol][12]['mean'] - results[vol][12]['std'],
                     results[vol][12]['mean'] + results[vol][12]['std'],
                     color=COLORS['protocol'], alpha=0.15)

    ax.set_xlabel('Time Steps', fontsize=13)
    ax.set_ylabel('Group Output', fontsize=13)
    ax.set_title('Monoculture vs. Diverse Groups Under Environmental Stress\n(σ = 0.10, 50 trials averaged)',
                 fontsize=14, fontweight='bold', pad=15)
    ax.legend(frameon=False, fontsize=12, loc='lower right')
    ax.set_ylim(0, 1.0)
    plt.savefig(os.path.join(OUT, 'mono-vs-diverse-timeseries.png'))
    plt.close()
    print("  [ok] mono-vs-diverse-timeseries.png")

    # --- CHART 3: Insurance effect — minimum output by diversity ---
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    for i, vol in enumerate(volatilities):
        mins = [results[vol][d]['min_output'] for d in diversities]
        ax.plot(diversities, mins, 'o-', color=vol_colors[i],
                label=vol_labels[i], linewidth=2, markersize=8)

    ax.set_xlabel('Number of Cultural Strategies', fontsize=13)
    ax.set_ylabel('Minimum Output (worst moment, avg of 50 trials)', fontsize=13)
    ax.set_title('The Insurance Effect: Diversity Raises the Floor\nMore strategies = higher worst-case output',
                 fontsize=14, fontweight='bold', pad=15)
    ax.legend(title='Environmental Volatility', frameon=False, fontsize=11)
    ax.set_xticks(diversities)
    ax.set_xticklabels(['1\n(Mono)', '3', '6', '12\n(Full)'])
    plt.savefig(os.path.join(OUT, 'insurance-effect-floor.png'))
    plt.close()
    print("  [ok] insurance-effect-floor.png")

    return results


# ============================================================
# CULTURAL RESILIENCE ABM
# ============================================================
def run_cultural_resilience():
    """Run the cultural resilience ABM and generate charts."""
    np.random.seed(42)

    class CulturalGroup:
        def __init__(self, gid, extraction, cooperation, pop=100):
            self.gid = gid
            self.extraction = np.clip(extraction, 0.05, 0.95)
            self.cooperation = np.clip(cooperation, 0.0, 0.95)
            self.pop = pop
            self.alive = True

        def step(self, resource_health, protocol_cap=None):
            if not self.alive:
                return 0, 0
            eff_ext = min(self.extraction, protocol_cap) if protocol_cap else self.extraction
            harvest = eff_ext * resource_health * self.pop * 0.01
            contribution = self.cooperation * harvest * 0.1
            growth = 0.02 * resource_health - 0.01 * (1 - resource_health)
            self.pop = max(1, self.pop * (1 + growth))
            if resource_health < 0.1:
                self.pop *= 0.9
            return harvest, contribution

    def run_scenario(name, groups, protocol_cap=None, steps=300):
        resource = 0.8
        history = {'resource': [], 'population': [], 'cultures': []}
        for t in range(steps):
            total_harvest = 0
            total_contribution = 0
            for g in groups:
                h, c = g.step(resource, protocol_cap)
                total_harvest += h
                total_contribution += c

            total_pop = sum(g.pop for g in groups if g.alive)
            depletion = total_harvest * 0.002
            regeneration = 0.05 * resource * (1 - resource) + total_contribution * 0.01
            resource = np.clip(resource - depletion + regeneration, 0, 1)

            history['resource'].append(resource)
            history['population'].append(total_pop)
            history['cultures'].append(sum(1 for g in groups if g.alive and g.pop > 5))

        return history

    # Three scenarios
    mono_groups = [CulturalGroup(i, extraction=0.5, cooperation=0.3) for i in range(3)]
    diverse_groups = [CulturalGroup(i,
                       extraction=np.random.uniform(0.2, 0.7),
                       cooperation=np.random.uniform(0.1, 0.6))
                      for i in range(12)]
    protocol_groups = [CulturalGroup(i,
                        extraction=np.random.uniform(0.2, 0.7),
                        cooperation=np.random.uniform(0.1, 0.6))
                       for i in range(12)]

    mono = run_scenario("Monoculture", mono_groups)
    diverse = run_scenario("Pure Diversity", diverse_groups)
    protocol = run_scenario("Protocol + Diversity", protocol_groups, protocol_cap=0.45)

    T = len(mono['resource'])

    # --- CHART 4: Resource health over time ---
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.plot(range(T), mono['resource'], color=COLORS['mono'],
            linewidth=2, label='Monoculture (3 identical groups)')
    ax.plot(range(T), diverse['resource'], color=COLORS['diverse'],
            linewidth=2, label='Pure Diversity (12 groups, no protocol)')
    ax.plot(range(T), protocol['resource'], color=COLORS['protocol'],
            linewidth=2, label='Thin Protocol + Thick Diversity')

    ax.set_xlabel('Time Steps', fontsize=13)
    ax.set_ylabel('Commons Resource Health', fontsize=13)
    ax.set_title('Three Strategies for Managing a Shared Commons\nAgent-Based Model, 300 steps',
                 fontsize=14, fontweight='bold', pad=15)
    ax.legend(frameon=False, fontsize=11, loc='lower right')
    ax.set_ylim(0, 1.0)
    ax.axhline(y=0.3, color='gray', linestyle='--', alpha=0.4, linewidth=0.8)
    ax.text(T * 0.98, 0.32, 'Collapse threshold', ha='right', fontsize=10, color='gray')
    plt.savefig(os.path.join(OUT, 'commons-resource-health.png'))
    plt.close()
    print("  [ok] commons-resource-health.png")

    # --- CHART 5: Population over time ---
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.plot(range(T), mono['population'], color=COLORS['mono'],
            linewidth=2, label='Monoculture')
    ax.plot(range(T), diverse['population'], color=COLORS['diverse'],
            linewidth=2, label='Pure Diversity')
    ax.plot(range(T), protocol['population'], color=COLORS['protocol'],
            linewidth=2, label='Thin Protocol + Thick Diversity')

    ax.set_xlabel('Time Steps', fontsize=13)
    ax.set_ylabel('Total Population', fontsize=13)
    ax.set_title('Population Dynamics Under Three Cultural Strategies',
                 fontsize=14, fontweight='bold', pad=15)
    ax.legend(frameon=False, fontsize=11)
    plt.savefig(os.path.join(OUT, 'population-dynamics.png'))
    plt.close()
    print("  [ok] population-dynamics.png")

    # --- CHART 6: Summary bar chart ---
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.5))
    scenarios = ['Monoculture', 'Pure Diversity', 'Protocol +\nDiversity']
    colors = [COLORS['mono'], COLORS['diverse'], COLORS['protocol']]

    # Final resource
    vals = [mono['resource'][-1], diverse['resource'][-1], protocol['resource'][-1]]
    axes[0].bar(scenarios, vals, color=colors, width=0.6)
    axes[0].set_ylabel('Resource Health')
    axes[0].set_title('Final Resource Health', fontweight='bold')
    axes[0].set_ylim(0, 1)

    # Final population
    vals = [mono['population'][-1], diverse['population'][-1], protocol['population'][-1]]
    axes[1].bar(scenarios, vals, color=colors, width=0.6)
    axes[1].set_ylabel('Population')
    axes[1].set_title('Final Population', fontweight='bold')

    # Cultural count
    vals = [mono['cultures'][-1], diverse['cultures'][-1], protocol['cultures'][-1]]
    axes[2].bar(scenarios, vals, color=colors, width=0.6)
    axes[2].set_ylabel('Surviving Cultures')
    axes[2].set_title('Cultural Diversity', fontweight='bold')

    for ax in axes:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    plt.suptitle('Thin Protocol + Thick Diversity: Best of Both Worlds',
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(os.path.join(OUT, 'three-strategies-summary.png'))
    plt.close()
    print("  [ok] three-strategies-summary.png")

    return mono, diverse, protocol


# ============================================================
# RUN ALL
# ============================================================
if __name__ == '__main__':
    print("Generating charts from emergence models...\n")

    print("Model A: Group Competition (Tilman Insurance Hypothesis)")
    run_group_competition()

    print("\nCultural Resilience ABM")
    run_cultural_resilience()

    print(f"\n[DONE] All charts saved to {OUT}/")
    print("   Embed in chapters with: ![caption](../images/filename.png)")

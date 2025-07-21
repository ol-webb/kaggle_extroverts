import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def apply_mappings(df, istest = False):

    stagefearmap = {'Yes': 1, 'No': 0}
    drainedmap = {'Yes': 1, 'No': 0}
    personalitymap = {'Extrovert': 1, 'Introvert': 0}

    df['Stage_fear'] = df['Stage_fear'].map(stagefearmap)
    df['Drained_after_socializing'] = df['Drained_after_socializing'].map(drainedmap)

    if not istest:
        df['Personality'] = df['Personality'].map(personalitymap)

    return df


def split_features(df):

    df['Time_Alone_greater3'] = df['Time_spent_Alone'] > 3
    df['Social_event_attendance_greater3'] = df['Social_event_attendance'] > 3
    df['Going_outside_greater3'] = df['Going_outside'] > 3
    df['Friends_circle_size_greater5'] = df['Friends_circle_size'] >= 5
    df['Post_frequency_greater2'] = df['Post_frequency'] > 2

    return df


def plot_graphs(df):

    fix, ax = plt.subplots(1,2, figsize = (8,3))

    sns.countplot(x = 'Stage_fear', data = df, hue = 'Personality', ax = ax[0])

    sns.countplot(x = 'Drained_after_socializing', data = df, hue = 'Personality', ax = ax[1])

    plt.show()


    fig, axs = plt.subplots(2,3, figsize = (9,6))

    for i, col in enumerate(['Time_spent_Alone', 'Social_event_attendance', 'Going_outside', 'Friends_circle_size', 'Post_frequency']):

        ax = axs.flat[i]
        sns.histplot(data = df, x = col, hue = 'Personality', ax = ax)

    plt.tight_layout()

    return


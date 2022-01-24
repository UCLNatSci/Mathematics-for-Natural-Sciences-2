#!/usr/bin/env python
# coding: utf-8

# ## Linear Transformations Python Code

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from myst_nb import glue

def make_axes():
    
    fig, axes = plt.subplots(1, 2, figsize=(9.5,4))
    fig.subplots_adjust(wspace=0.5)
    fig.text(0.5, 0.5, "$T$", fontsize=20, ha="center")
    fig.text(0.5, 0.4, "$\longrightarrow$", fontsize=30, ha="center")
    for ax in axes:
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_xticks([-2, -1, 0, 1, 2])
        ax.set_yticks([-2, -1, 0, 1, 2])
        ax.grid()
        ax.set_axisbelow(True)
    
    return fig, axes

def plot_vector(ax, x, y):
    ax.arrow(0, 0, x, y, width=0.03, color="black", length_includes_head=True)
    
def add_text(ax, x, y, s):
    ax.text(x, y, s, fontsize=16)


# In[2]:


fig, (ax1, ax2) = make_axes()
plot_vector(ax1, 1, 0)
add_text(ax1, 0.7, -0.4, "$e_1$")
plot_vector(ax1, 0, 1)
add_text(ax1, -0.5, 0.9, "$e_2$")
plot_vector(ax2, -1, 0)
add_text(ax2, -1, -0.4, "$T(e_1)$")
plot_vector(ax2,0, 1)
add_text(ax2, 0.1, 0.8, "$T(e_2)$")

glue("la_fig_1", fig, display=False)


# In[3]:


fig, (ax1, ax2) = make_axes()
plot_vector(ax1, 1, 0)
add_text(ax1, 0.7, -0.4, "$e_1$")
plot_vector(ax1, 0, 1)
add_text(ax1, -0.5, 0.9, "$e_2$")

ax1.plot([1, 1], [0, 1], lw=2, ls=":", color="black")
ax1.plot([0, 1], [1, 1], lw=2, ls=":", color="black")
add_text(ax1, 0.7, 1.2, "$e_1+e_2$")

plot_vector(ax2, -1, 0)
add_text(ax2, -1, -0.4, "$T(e_1)$")
plot_vector(ax2,0, 1)
add_text(ax2, 0.1, 0.8, "$T(e_2)$")

ax2.plot([-1, -1], [0, 1], lw=2, ls=":", color="black")
ax2.plot([-1, 0], [1, 1], lw=2, ls=":", color="black")
add_text(ax2, -1.9, 1.2, "$T(e_1)+T(e_2)$")


glue("la_fig_2", fig, display=False)


# In[4]:


fig, (ax1, ax2) = make_axes()

plot_vector(ax1, 1, 0)
add_text(ax1, 0.7, -0.4, "$e_1$")
plot_vector(ax1, 0, 1)
add_text(ax1, -0.5, 0.9, "$e_2$")

ax1.plot([-2, 2], [2, -2], lw=2, ls="--", color="silver", zorder=0)

plot_vector(ax2, 0, -1)
add_text(ax2, -1.5, -0.4, "$T(e_2)$")
plot_vector(ax2, -1, 0)
add_text(ax2, 0.1, -1, "$T(e_1)$")

ax2.plot([-2, 2], [2, -2], lw=2, ls="--", color="silver", zorder=0)


glue("la_fig_3", fig, display=False)


# In[5]:


fig, (ax1, ax2) = make_axes()

plot_vector(ax1, 1, 0)
add_text(ax1, 0.7, -0.4, "$e_1$")
plot_vector(ax1, 0, 1)
add_text(ax1, -0.5, 0.9, "$e_2$")

theta = np.pi/6
ct = np.cos(theta)
st = np.sin(theta)

plot_vector(ax2, ct, st)
add_text(ax2, -.7, 1, "$T(e_2)$")
plot_vector(ax2, -st, ct)
add_text(ax2, 0.5, 0.7, "$T(e_1)$")


ax2.plot([0, ct], [0, 0], lw=2, ls=":", color="black")
ax2.plot([ct, ct], [0, st], lw=2, ls=":", color="black")

ax2.plot([0, -st], [0, 0], lw=2, ls=":", color="black")
ax2.plot([-st, -st], [0, ct], lw=2, ls=":", color="black")

ax2.text(1, 0.2, "$\sin\\theta$", fontsize=12)
ax2.text(-1.2, 0.4, "$\cos\\theta$", fontsize=12)

ax2.text(-.5, -0.3, "$\sin\\theta$", fontsize=12)
ax2.text(.2, -0.3, "$\cos\\theta$", fontsize=12)

glue("la_fig_4", fig, display=False)


# In[ ]:





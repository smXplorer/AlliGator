.. _alligator-python-plugin-publication:

Publishing an AlliGator Python Plugin
+++++++++++++++++++++++++++++++++++++

Writing a plugin for AlliGator should be fairly simple based on the provided 
examples. Using it with your installation of AlliGator is as simple as copying 
it in the *Python Plugins* folder and resetting the Python session in the 
**Settings:Plugins** panel.

To make your plugin available to others, it is recommended to publish it on 
GitHub (or any other publicly accessible repository) using the template provided 
at `https://github.com/smXplorer/AlliGator-Plugin-Template 
<https://github.com/smXplorer/AlliGator-Plugin-Template>`_.

If possible, name your repository "AlliGator-Plugin-my-plugin-name" in order for 
it to be easily searchable on GitHub (or found by search engines).

An AlliGator Python Plugin repository should contain at least 3 mandatory files:

+ A Python script (\*.py file) containing the function(s) to be called by 
  AlliGator. This script/function(s) should comply with the API as described in 
  AlliGator's :ref:`AlliGator Python Plugin manual page <alligator-python-plugin>`.

+ A *license.txt* file (the default license is BSD 3-Clause) with the correct 
  copyright holder name and date

+ A *Readme.md* file modified to be relevant to your plugin (in particular, the 
  content of the template *Readme.md* file should be removed and replaced by 
  your own content). The role of the *Readme.md* file is to provide basic 
  information on the plugin and preferably enough information on how to use it. 
  Instructions on how to use the plugin, or links to a website/URL providing 
  these instructions would belong to the Readme file. A simple guide to the 
  markup language used in \*.md file can be found 
  `here <https://www.markdownguide.org/basic-syntax/>`_.

If possible, provide files to test the plugin in a *data* folder within the 
repository, and if appropriate, results from the analysis (e.g. screenshot of 
outputs, AlliGator notebook, plot files, etc.) in a *results* folder.

It is recommended to store images used to illustrate the Readme file in an 
*images* folder in the repository.

An example of such a repository with these different elements can be found `here 
<https://github.com/smXplorer/AlliGator-Plugin-IntensityOverThresholdMask>`_
# Stats badge

Simple github profile languages stats badges.\
The project __automatically__ generates a new personal badge every 6 hours.

<img src="https://nf-coder.github.io/stats-badge/out.svg">

## Quick start
To use this project you should:
1. Fork it
2. Go to Settings -> Github Pages and change souce to `GitHub Actions`
<img width="758" height="427" alt="Снимок экрана от 2025-11-15 21-22-09" src="https://github.com/user-attachments/assets/fb4896be-9b2c-440c-a5c4-75669a47506f" style="margin: auto"/>

3. Then go to Actions and click `I understand my workflows, go ahead and enable them`
<img width="649" height="369" alt="Снимок экрана от 2025-11-15 21-28-24" src="https://github.com/user-attachments/assets/95d245bd-c37e-4fd3-a366-a57f0bf582c2" style="margin: auto"/>

4. Then enable `Update SVG and Deploy to Pages` action and run it (you should to do this only first time)
<img width="1585" height="237" alt="Снимок экрана от 2025-11-15 21-28-43" src="https://github.com/user-attachments/assets/eeb8f214-174b-42ab-b202-6291c156625c" style="margin: auto"/>
<img width="1219" height="496" alt="Снимок экрана от 2025-11-15 21-28-55" src="https://github.com/user-attachments/assets/0cf68d59-8029-42f7-9232-f0b09226ef15" style="margin: auto"/>

Then you can use it with
```html
<img src="https://your-gh-page-url/out.svg">
```
<img src="https://nf-coder.github.io/stats-badge/out.svg">

## Configuring
Example config u can see in `setting.yaml`
```yaml
general:
  top_k: 4                      # how many sections will be on donut-chart (including "Other" section)
  plane:
    height: 140                 # height of svg
    width: 250                  # width of svg
  coloring:
    type: "github"              # type of coloring (github or oklch available)
    other_color: "#666666"      # color of "Other" section
  # coloring:
  #   type: "oklch"             # type of coloring (github or oklch available)
  #   chroma: 0.099             # coloring oklch chroma
  #   lightness: 0.636          # coloring oklch lightness
  #   other_color: "#666666"    # color of "Other" section
  excluded_languages:           # list of languages that should be excluded
    - Jupyter Notebook          # removed because jupyter files are too large

legend:
  margin_x: 140                 # margin of legend (x-axis)
  margin_y: 30                  # margin of legend (y-axis)
  space_between_captions: 22    # space between legend options
  font_color: "#c1c1c1"         # font color

diagram:
  outer_radius: 55              # outer circle radius
  thickness: 12                 # size of donut-chart
  margin_x: 20                  # margin of diagram (x-axis)
  margin_y: 15                  # margin of diagram (y-axis)
```
About **oklch** u can read [here](https://oklch.com/)

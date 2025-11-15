# Stats badge

Simple github profile languages stats badges.\
The project __automatically__ generates a new personal badge every 2 hours.

## Quick start
To use this project you should only fork it!\
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

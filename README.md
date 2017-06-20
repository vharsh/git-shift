## Intro

- A small git utility to collaborate with your team without knowing git.

## Example Usage

```python
import git
git.save(msg = 'Fixes overlapping text on graph.')
git.upload() # Considers default remote as :origin and default branch as :master
```

### TODO

- gracefully report errors and point to helpful solutions for the git-newbie
- frictionless additiono of useful files?
- handling merge conflicts?
- a fetch before a push?

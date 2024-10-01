# Functions (maybe call these flows so it's not so confusing)

main.py is core logic that uses the "new issue" trigger. Do all of the intial triage and filtering here.
recommended to put as many reusable functions in their own files as possible.

#### Example
"New Issue" Trigger
- main.py runs
  - Okta alert identified
  - Okta investigation function runs
  - esclation = false
  - Issue closed

`Okta Investigation` should be its own flow comprised of other smaller function calls for okta information
`Issue closed` should also be it's own flow that closes the issue.

#! /bin/bash
AGENT_URL=${AGENT_URL:-"http://ec2-3-232-182-160.compute-1.amazonaws.com:10004"}
ASSIGNED_SUBJECTS=${ASSIGNED_SUBJECTS:-"all"}

python evaluate_from_api.py --agent_url $AGENT_URL --assigned_subjects $ASSIGNED_SUBJECTS
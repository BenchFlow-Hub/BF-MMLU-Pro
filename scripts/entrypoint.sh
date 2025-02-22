#! /bin/bash
AGENT_URL=${AGENT_URL}
TEST_START_IDX=${TEST_START_IDX:-"all"}

python evaluate_from_api.py --agent_url $AGENT_URL --assigned_subjects $TEST_START_IDX
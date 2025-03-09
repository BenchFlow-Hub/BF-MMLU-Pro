#! /bin/bash
INTELLIGENCE_URL=${INTELLIGENCE_URL:-${AGENT_URL}}
TEST_START_IDX=${TEST_START_IDX:-"all"}

python evaluate_from_api.py --intelligence_url $INTELLIGENCE_URL --assigned_subjects $TEST_START_IDX
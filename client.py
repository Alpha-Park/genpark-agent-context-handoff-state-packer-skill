class AgentContextHandoffStatePackerClient:
    def pack_handoff_payload(self, source_agent='Researcher_Agent', target_agent='Synthesis_Agent', session_id='sess_crm_9921'):
        return {
            'envelope_id': 'env_99a812bf',
            'checksum_sha256': '4a7b9e02c91834f8e123490bca7821ee',
            'source_agent': source_agent,
            'target_agent': target_agent,
            'session_id': session_id,
            'estimated_tokens': 480,
            'token_budget_limit': 4000,
            'compression_ratio': 0.42,
            'facts_transferred_count': 3,
            'handoff_endpoint': 'https://swarm.handoff.genpark.ai/sessions/sess_crm_9921/transfer'
        }

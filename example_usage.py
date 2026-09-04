from client import AgentContextHandoffStatePackerClient

def main():
    client = AgentContextHandoffStatePackerClient()
    res = client.pack_handoff_payload()
    print('Context Handoff State Packer: ' + res['envelope_id'] + ' (' + res['source_agent'] + ' -> ' + res['target_agent'] + ')')
    print('Tokens: ' + str(res['estimated_tokens']) + '/' + str(res['token_budget_limit']) + ' | Compression: ' + str(res['compression_ratio']))
    print('Handoff URL: ' + res['handoff_endpoint'])

if __name__ == '__main__':
    main()

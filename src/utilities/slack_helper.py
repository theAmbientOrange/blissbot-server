def get_entity_details(slack_bot_client, entity_id):
    entity_details = {
        'channel': '',
        'real_name': ''
    }

    # Handle user
    if entity_id[0] == 'U':
        users_info_response = slack_bot_client.api_call(
            'users.info',
            user=entity_id
        )
        if users_info_response['ok']:
            entity_details['channel'] = users_info_response['user']['name']
            entity_details['real_name'] = users_info_response['user']['real_name']
            return entity_details
        else:
            print('SEND NO USER FOUND MESSAGE')
            return None

    # Handle channel
    elif entity_id[0] == 'C':
        conversations_info_response = slack_bot_client.api_call(
            'conversations.info',
            channel=entity_id
        )
        if conversations_info_response['ok']:
            entity_details['channel'] = conversations_info_response['channel']['id']
            entity_details['real_name'] = '#' + \
                conversations_info_response['channel']['name_normalized']
            return entity_details
        else:
            print('SEND NO CHANNEL FOUND MESSAGE')
            return None

    # Unknown selection made :-(
    else:
        print('Oh noooose')
        return None
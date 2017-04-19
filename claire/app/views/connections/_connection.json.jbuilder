json.extract! connection, :id, :user_id, :ip_address, :username, :password, :created_at, :updated_at
json.url connection_url(connection, format: :json)
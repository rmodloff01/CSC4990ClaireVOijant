json.extract! video, :id, :user_id, :file_name, :created_at, :updated_at
json.url video_url(video, format: :json)
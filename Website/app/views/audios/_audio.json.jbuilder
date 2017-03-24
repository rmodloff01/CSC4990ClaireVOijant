json.extract! audio, :id, :user_id, :file_name, :title, :status, :created_at, :updated_at
json.url audio_url(audio, format: :json)
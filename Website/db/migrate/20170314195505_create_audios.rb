class CreateAudios < ActiveRecord::Migration[5.0]
  def change
    create_table :audios do |t|
      t.string :user_id
      t.string :file_name
      t.string :title
      t.boolean :status

      t.timestamps
    end
  end
end

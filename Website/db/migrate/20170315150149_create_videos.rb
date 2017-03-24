class CreateVideos < ActiveRecord::Migration[5.0]
  def change
    create_table :videos do |t|
      t.integer :user_id
      t.string :file_name

      t.timestamps
    end
  end
end

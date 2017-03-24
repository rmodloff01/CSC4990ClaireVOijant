class CreateLights < ActiveRecord::Migration[5.0]
  def change
    create_table :lights do |t|
      t.string :file_name
      t.boolean :status

      t.timestamps
    end
  end
end

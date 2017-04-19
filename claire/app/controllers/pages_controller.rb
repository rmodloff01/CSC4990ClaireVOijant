class PagesController < ApplicationController 
	before_action :authenticate_user!

  def home
  end

  #method for running sendemailpic,  modified to stop streaming before and restart after 
  def getpic
    @email = params[:u_email]
  	system("sendemailpic " + @email + "") or raise "Something went wrong."
  	redirect_to :back
  end

  #method for running sendemailvid, modified to stop streaming before and restart after 
  def getvid
    #system("pkill ffserver") or raise "Something went wrong."
    @email = params[:u_email]
  	system("sendemailvid " + @email + "") or raise "Something went wrong."
  	redirect_to :back
  end

  #method for recording sound
  def recsound
    system("recsound") or raise "Something went wrong."
    redirect_to :back
  end

  #method for live stream (WE MAY NOT NEED THIS IF WE ARE ALWAYS STREAMING)
  def livestream
    system("/home/pi/bin/startstream") or raise "Something went wrong."
    redirect_to :back
  end

  #method for playing random sound
  def randsound
    system("rndsound") or raise "Something went wrong."
    redirect_to :back
  end

    #method for stopping sound output
  def stopsound
    system("stopsound") or raise "Something went wrong."
    redirect_to :back
  end

  def gallery
    @images = Dir.glob("app/assets/images/pictures/*.jpg")
  end

  def sendit
      @email = params[:u_email]
      @img_name = params[:img_name]
      system("./sendpictoemail " + @email + @img_name)
      redirect_to :back
    end

end
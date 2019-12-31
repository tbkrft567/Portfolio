class MembersController < ApplicationController
  before_action :authorize

  def create
    p params[:id]
    @group = Group.find_by(id: params[:id])
    @member = Member.new(user: current_user, group: @group)
    if @member.valid?
      @allMembers = Member.where(user: current_user, group: @group).exists?
      unless @allMembers
        p "save"
        @member.save
      else
        flash[:alert] = ['You can only be added once']
      end
    else
        flash[:alert] = @member.errors.full_messages
    end
    redirect_to groups_show_path(id: params[:id])
  end

  def destroy
    group = Group.find_by(id: params[:id])
    members = Member.where(user: current_user).where(group: group)
    if members
        members.destroy_all
    else
        flash[:alert] = ['This cannot be removed']
    end
    redirect_to groups_show_path(id: params[:id])
  end
end

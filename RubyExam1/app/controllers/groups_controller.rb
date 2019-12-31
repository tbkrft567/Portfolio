class GroupsController < ApplicationController
  def create
    @group = Group.new(secureGroup)
    if @group.valid?
      @group.save
      @newGroup = Group.last
      @creator = @newGroup.user
      @member = Member.new(user: @creator, group: @newGroup)
      if @member.valid?
        @member.save
      else
        flash[:alert] = @member.errors.full_messages
      end
    else
      flash[:alert] = @group.errors.full_messages
    end
    redirect_to groups_index_path
  end
  
  def destroy
    @group = Group.find_by(id: params[:id])
    if @group && @group.user == current_user
      @group.destroy
    else
      flash[:alert] = ['This group cannot be deleted']
    end
    redirect_to groups_index_path
  end

  def show
    @group = Group.find_by(id: params[:id])
    if @group
      @user = current_user
      @members = @group.user_members
    else
      redirect_to groups_index_path
    end
  end

  def index
    @user = current_user
    @groups = Group.all
  end
end

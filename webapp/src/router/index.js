import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'

import ImagesGet from '@/components/images/ImagesGet'
import ImagesAdd from '@/components/images/ImagesAdd'
import ImagesEdit from '@/components/images/ImagesEdit'
import ImagesDelete from '@/components/images/ImagesDelete'

import MenusGet from '@/components/menus/MenusGet'
import MenusAdd from '@/components/menus/MenusAdd'
import MenusEdit from '@/components/menus/MenusEdit'
import MenusDelete from '@/components/menus/MenusDelete'

import GroupsGet from '@/components/groups/GroupsGet'
import GroupsAdd from '@/components/groups/GroupsAdd'
import GroupsEdit from '@/components/groups/GroupsEdit'
import GroupsDelete from '@/components/groups/GroupsDelete'

import OrganizationsGet from '@/components/organizations/OrganizationsGet'
import OrganizationsAdd from '@/components/organizations/OrganizationsAdd'
import OrganizationsEdit from '@/components/organizations/OrganizationsEdit'
import OrganizationsDelete from '@/components/organizations/OrganizationsDelete'

import UsersGet from '@/components/users/UsersGet'
import UsersAdd from '@/components/users/UsersAdd'
import UsersEdit from '@/components/users/UsersEdit'
import UsersDelete from '@/components/users/UsersDelete'

Vue.use(Router)

export default new Router({
  routes: [
    {path: '/', name: 'Home', component: Home},
    {path: '/home', name: 'Home', component: Home},
    {path: '/imagesget', name: 'ImagesGet', component: ImagesGet},
    {path: '/imagesadd', name: 'ImagesAdd', component: ImagesAdd},
    {path: '/imagesedit', name: 'ImagesEdit', component: ImagesEdit},
    {path: '/imagesdelete', name: 'ImagesDelete', component: ImagesDelete},
    {path: '/menusget', name: 'MenusGet', component: MenusGet},
    {path: '/menusadd', name: 'MenusAdd', component: MenusAdd},
    {path: '/menusedit', name: 'MenusEdit', component: MenusEdit},
    {path: '/menusdelete', name: 'MenusDelete', component: MenusDelete},
    {path: '/groupsget', name: 'GroupsGet', component: GroupsGet},
    {path: '/groupsadd', name: 'GroupsAdd', component: GroupsAdd},
    {path: '/groupsedit', name: 'GroupsEdit', component: GroupsEdit},
    {path: '/groupsdelete', name: 'GroupsDelete', component: GroupsDelete},
    {path: '/organizationsget', name: 'OrganizationsGet', component: OrganizationsGet},
    {path: '/organizationsadd', name: 'OrganizationsAdd', component: OrganizationsAdd},
    {path: '/organizationsedit', name: 'OrganizationsEdit', component: OrganizationsEdit},
    {path: '/organizationsdelete', name: 'OrganizationsDelete', component: OrganizationsDelete},
    {path: '/usersGet', name: 'UsersGet', component: UsersGet},
    {path: '/usersadd', name: 'UsersAdd', component: UsersAdd},
    {path: '/usersedit', name: 'UsersEdit', component: UsersEdit},
    {path: '/usersdelete', name: 'UsersDelete', component: UsersDelete}
  ]
})

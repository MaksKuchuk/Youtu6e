import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import RegisterView from '../views/RegisterView.vue';
import LoginView from '../views/LoginView.vue';
import VideoView from '../views/VideoView.vue';
import ChannelView from '../views/ChannelView.vue';
import SubscribersView from '../views/SubscribersView.vue';
import PlaylistView from '../views/PlaylistView.vue';
import ChannelVideosView from '../views/CnannelVideosView.vue';
import StudioView from '../views/StudioView.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/video/:id',
    name: 'video',
    component: VideoView,
  },
  {
    path: '/channel/:id',
    name: 'channel',
    component: ChannelView,
  },
  {
    path: '/subscribers/:id',
    name: 'subscribers',
    component: SubscribersView,
  },
  {
    path: '/playlist/:id',
    name: 'playlist',
    component: PlaylistView,
  },
  {
    path: '/channel/videos/:id',
    name: 'videos_channel',
    component: ChannelVideosView,
  },
  {
    path: '/studio',
    name: 'studio',
    component: StudioView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

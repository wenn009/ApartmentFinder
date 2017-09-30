import Base from './Base/Base';
import App from './App/App';
import CustomerUpdate from './CustomerUpdate/CustomerUpdate';


const routes = {
  component: Base,
  childRoutes: [
    {
      path: '/',
      component: App
    },

    {
      path: '/subscribe',
      component: CustomerUpdate
    }
  ]
};

export default routes;
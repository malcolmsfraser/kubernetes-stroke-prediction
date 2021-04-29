import http from 'k6/http';
import { sleep } from 'k6';

const url = "http://20.81.8.9/predict";
const data = require('payload.json');

export const options = {
  duration: '1m',
  vus: 10,
  thresholds: {
    http_req_duration: ['p(95)<2500'],
  },
};

export default function () {
    let res = http.post(url, JSON.stringify(data),
                       { headers: { 'Content-Type': 'application/json' } });
    console.log(res);
  sleep(1);
}

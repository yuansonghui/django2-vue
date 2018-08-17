import request from '@/utils/request'
import apiPath from './apiPath'

export function baseApi(params) {
  if (!params.method) {
    params.method = 'post'
  }
  return request({
    url: apiPath[params.functionName],
    method: params.method,
    data: params.data
  }).then(data => {
    return data
  })
}
class FilterResults:

    def __init__(self, results_list, params):
        self.results_list = results_list
        self.params = params
        self.match_list = self.filter_results(self.results_list)


    def filter_results(self, results):
        match_list = []
        for result in results:
            if result['price'] <= self.params['max_price'] and result['duration'] >= self.params['min_duration']:
                match_list.append(result)
        if len(match_list) == 0:
            return False
        else:
            return match_list



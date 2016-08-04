def store(data,*full_names):
    for full_names in full_names:
        names = full_names.split()
        if len(names) == 2:names.insert(1,'')
        labels = 'first','middle','last'
        for label,name in zip(labels,names):
            people = loolup(data,label,name)
            if people:
                people.append(full_names)
            else:
                data[label][name] = [full_names]

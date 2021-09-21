
use game;


declare
 @dat date,
 @platform varchar(10),
 @dao int, 
 @wau int

--������� ������� ��� ����������
create table result2
(
  platform varchar(15),
  Date date,
  DAO int,
  WAU int
  )

DECLARE c CURSOR  
    FOR select distinct Convert(varchar(10), cast(eventTimestamp as Date), 101) as d, platform
		from metric
		order by platform, d
OPEN c  
FETCH NEXT FROM c into @dat, @platform

--����, ��� ��������, ���� ���� ����������� �� � ��������, � �������� ������� ��������� ����� � ����� ���������  
declare
 @d int,
 @p_last varchar(10)

 select @d = (DATEDIFF(DAY,0, @dat)%7+1), @p_last = '-'
 
--����� ���������� � ����, ���� �������� �� � �������
while @@fetch_status=0
    begin 

		--1.1
		select @dao = count(t.id) 
		from 
			(
			select distinct userID as id
			from metric
			where platform = @platform
				and Convert(varchar(10), cast(eventTimestamp as Date), 104) = @dat) t;

		--1.2
		--��� ��������� �������������� � ��������, � �� ������� � ���� ���� �����������
		if (DATEDIFF(DAY,0, @dat)%7+1) = 1
			begin
				select @wau = count(distinct m.userID) 
				from metric m
				where platform = @platform
					and Convert(varchar(10), cast(eventTimestamp as Date), 104) >= @dat
					and cast( Convert(varchar(10), cast(eventTimestamp as Date), 104) as Date) < 
						cast( Convert(varchar(10), DATEADD(day, 7, @dat), 104) as Date);
			end;

		--��� ��������, ���� ��� ��������� �������������� �� � �������� 
		if @p_last <> @platform and (DATEDIFF(DAY,0, @dat)%7+1) <> 1
			begin
				select @wau = count(distinct m.userID) 
				from metric m
				where platform = @platform
					and Convert(varchar(10), cast(eventTimestamp as Date), 104) >= @dat
					and cast( Convert(varchar(10), cast(eventTimestamp as Date), 104) as Date) < 
						cast( Convert(varchar(10), DATEADD(day, 8 - @d, @dat), 104) as Date);
			end;
	
	insert into result2
		(platform, Date, DAO, WAU)
	VALUES
		(@platform, @dat, @dao, @wau);

	select @p_last = @platform, @d = (DATEDIFF(DAY,0, @dat)%7+1)
	FETCH NEXT FROM c into @dat, @platform

	end;


close c
deallocate c;

select * from result2;

/*
drop table result2;
--*/
